$: << __dir__

require_relative "proto/crewgenerator_services_pb"

@stub = Crewgen::CrewGenerator::Stub.new("localhost:9452", :this_channel_is_insecure)

request = Crewgen::GenerateHtmlGameRequest.new(
  name: "Four-Letter Word Guessing Game",
  description: "The client envisions a Wordle-inspired game where the target word can vary between 3 to 5 letters. Players will have up to 10 guesses to identify the correct word. To aid players, an alphabet chart will be provided, utilizing color-coded indicators: grey for unseen letters, red for incorrect letters, green for correct letters in the right position, and yellow for correct letters in the wrong position. The game aims to enhance the typical Wordle experience while maintaining a similar core mechanic, adding a twist with variable word lengths. No additional features or mechanics such as themed word lists, daily challenges, or power-ups have been specified, but these can be considered in future conversations to enrich the player experience."
)

response = @stub.generate_html_game(request)
puts response.html.data
File.write("output.html", response.html.data)
