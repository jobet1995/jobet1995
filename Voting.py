class Candidate:
  def __init__(self, name):
    self.name = name
    self.votes = 0

  def cast_vote(self):
    self.votes += 1

class VotingSystem:
  def __init__(self):
    self.candidates = {}

  def add_candidate(self, candidate):
    self.candidates[candidate.name] = candidate

  def cast_vote(self, candidate_name):
    if candidate_name in self.candidates:
      self.candidates[candidate_name].cast_vote()
    else:
      print("Invalid candidate")

  def get_winner(self):
    winner = None
    winner_votes = 0
    for candidate in self.candidates.values():
      if candidate.votes > winner_votes:
        winner = candidate
        winner_votes = candidate.votes
    return winner

# Initialize the voting system and candidates
voting_system = VotingSystem()
candidate_1 = Candidate("Candidate 1")
candidate_2 = Candidate("Candidate 2")
voting_system.add_candidate(candidate_1)
voting_system.add_candidate(candidate_2)

# Main voting loop
while True:
  # Prompt the user to cast their vote
  print("Please cast your vote:")
  print("1. Candidate 1")
  print("2. Candidate 2")
  print("3. Exit")
  choice = input("Enter your choice: ")

  # Cast the vote and update the vote count
  if choice == '1':
    voting_system.cast_vote("Candidate 1")
  elif choice == '2':
    voting_system.cast_vote("Candidate 2")
  elif choice == '3':
    break
  else:
    print("Invalid choice. Please try again.")

# Save the vote count to a file
with open("vote_count.txt", "w") as f:
  for candidate in voting_system.candidates.values():
    f.write(f"{candidate.name}: {candidate.votes} votes\n")

# Determine the winner
winner = voting_system.get_winner()
if winner:
  print(f"{winner.name} wins!")
else:
  print("The election is a tie!")
