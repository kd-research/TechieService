$: << __dir__

require_relative "proto/crewgenerator_services_pb"

@stub = Crewgen::CrewGenerator::Stub.new("localhost:9452", :this_channel_is_insecure)

request = Crewgen::GenerateHtmlGameRequest.new(
  name: "Four-Letter Word Guessing Game",
  description: "The client is interested in creating a new word game where users are asked to guess a 4-letter word. The game should provide more nuanced feedback beyond merely indicating which letters are correct and in the correct position. The client wants a feedback system that also indicates letters that are correct but in the wrong position, as well as letters that are incorrect. The gameplay involves: 1. A user guessing a 4-letter word. 2. The system providing feedback: - Correct letters in the correct position. - Correct letters in the wrong position, highlighted separately. - Incorrect letters, also highlighted separately. The game should have a fixed number of attempts (e.g., 10 attempts), and the feedback for each guess should include: - The guess with correct letters in the correct position. - Symbols indicating correct letters in the wrong position. - A list of wrong position letters on the side. - A list of incorrect letters on the side. The client's ultimate goal is to create a more engaging and informative guessing game that enhances user experience by offering detailed and helpful feedback after each guess. The provided Python code in the conversation implements this enhanced feedback mechanism, showing correct letters, wrong-position letters, and incorrect letters separately. The user is informed after each guess and continues until the word is correctly guessed or attempts run out."
)

response = @stub.generate_html_game(request)
puts response.html.data
File.write("output.html", response.html.data)
