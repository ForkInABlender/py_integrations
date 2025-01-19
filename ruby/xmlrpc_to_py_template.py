# Dylan Kenneth Eliot

# this is template for the python code; it works even for a stripped down rpc....


require 'xmlrpc/server'

server = XMLRPC::Server.new(8080)

class RubyService
  def say_hello(name)
    "Hello, #{name} from Ruby!"
  end

  def add_numbers(a, b)
    a + b
  end
end

server.add_handler("ruby_service", RubyService.new)

# Keep the server running
trap("INT") { exit }
server.serve
