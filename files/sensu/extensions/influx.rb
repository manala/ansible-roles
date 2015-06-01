require 'rubygems' if RUBY_VERSION < '1.9.0'
require 'influxdb'
require 'timeout'
require 'json'

module Sensu::Extension

  class Influx < Handler

    def name
      'influx'
    end

    def description
      'outputs metrics to InfluxDB'
    end

    def post_init
      @influxdb = InfluxDB::Client.new settings['influx']['database'], :host => settings['influx']['host'], :port => settings['influx']['port'], :username => settings['influx']['user'], :password => settings['influx']['password']
      @timeout = @settings['influx']['timeout'] || 15
      @prefix = @settings['influx']['prefix'] || ""
    end

    def run(event)
      begin
        event = JSON.parse(event)
        host = event['client']['name']
        series = @prefix + "host." + host
        timestamp = event['check']['issued']
        duration = event['check']['duration']
        output = event['check']['output']
      rescue => e
        @logger.error("InfluxDB: Error setting up event object - #{e.backtrace.to_s}")
      end

      begin
        output.split(/\n/).each do |line|
          @logger.debug("Parsing line: #{line}")
          k,v,t = line.split(/\s+/)
          k = k.split('.', 2)[1] #remove host and metric name
          v = v.match('\.').nil? ? Integer(v) : Float(v) rescue v.to_s
          point = {:time => t.to_f, :value => v}
          begin
            @influxdb.write_point(series + "." + k, point, true)
          rescue => e
            @logger.error("InfluxDB: Error posting event - #{e.backtrace.to_s}")
          end
        end
      rescue => e
        @logger.error("InfluxDB: Error parsing output lines - #{e.backtrace.to_s}")
        @logger.error("InfluxDB: #{output}")
      end

      yield("InfluxDB: Handler finished", 0)
    end

  end
end
