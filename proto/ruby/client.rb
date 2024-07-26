$: << __dir__

require_relative "proto/crewgenerator_services_pb"

@stub = Crewgen::CrewGenerator::Stub.new("localhost:9452", :this_channel_is_insecure)

request = Crewgen::GenerateHtmlGameRequest.new(
  name: "Four-Letter Word Guessing Game",
  description: "The Four-Letter Word Guessing Game is a fun and challenging word puzzle that tests players' vocabulary and deduction skills. The objective of the game is to guess a hidden four-letter word within five attempts, using clues provided after each guess to guide the player towards the correct answer. The game should have different word to guess each time it is played.",
)

response = @stub.generate_html_game(request)
puts response.html.data
File.write("output.html", response.html.data)
