# Creating the class for text_editor
class text_editor:

    # Setting up base stuff
    def __init__(self):
        self._phrase = None
        self._space = None
        command = ""

        # Continue until the users prompts it to stop
        while command != "Stop":

            # Specifies the available prompts for the user
            command = input("Enter a command (Start, Right, Left, Insert, Delete, Stop): ")

            # When the prompt is Start
            if command == "Start":
                # Generate the interface to collect the User's phrase
                print("Write your text down below:")
                self._phrase = input()

                # Generate the line with the cursor object
                self._space = self.space_line(self._phrase)

                # Prints said line
                print(self._space)

            # When the prompt is Right
            elif command == "Right":

                # If there is no prompt, throws an error
                if self._phrase is None:
                    print("No text input has been given")

                else:
                    # Generates a new cursor object line using the move_right function
                    self._space = self.move_right(self._space)

                    # Prints the phrase and new cursor object line
                    print(self._phrase)
                    print(self._space)

            # When the prompt is Left
            elif command == "Left":

                # If there is no prompt, throws an error
                if self._phrase is None:
                    print("No text input has been given")

                else:
                    # Generates a new cursor object line using the move_left function
                    self._space = self.move_left(self._space)

                    # Prints the phrase and new cursor object line
                    print(self._phrase)
                    print(self._space)

            # When the prompt is Insert
            elif command == "Insert":

                # If there is no prompt, throws an error
                if self._phrase is None:
                    print("No text input has been given")

                else:
                    # Prompts the user for the character they want to add
                    print("Insert 1 character")
                    character = input()

                    # Using the insert function, a new phrase is created witht the character included
                    self._phrase = self.insert(self._phrase, self._space, character)

                    # A new cursor object line is created based on the new phrase
                    self._space = self.space_line(self._phrase)

                    # The phrase and new cursor object line are printed
                    print(self._phrase)
                    print(self._space)

            # When the prompt is Delete
            elif command == "Delete":

                # If there is no prompt, throws an error
                if self._phrase is None:
                    print("No text input has been given")

                # If the cursor object is at the end of the phrase nothing is deleted
                elif self._space[-1] == "^":
                    print(self._phrase)
                    print(self._space)

                else:
                    # The delete function modifies the previous phrase, which then gets reassigned to the "phrase" pbject
                    self._phrase = self.delete(self._phrase)

                    # A new cursor object line is created based on the new phrase
                    self._space = self.space_line(self._phrase)

                    # The phrase and new cursor object line are printed
                    print(self._phrase)
                    print(self._space)

            elif command == "Stop":
                # Generates the final output for the user
                print("")
                print("The program has stopped.")
                print(f"Your final phrase was: {self._phrase}")

            else:
                print("Invalid command. Please enter a valid command.")


    def space_line(self, phrase):
        # Generating the cursor object line for the positional
        # character
        individual_characters = [" " for char in phrase]

        # Adding the cursor object to the cursor object line
        individual_characters[0] = "^"

        # Combining cursor object line
        combined_string = "".join(individual_characters)

        # Returning the cursor object line
        return combined_string


    def move_right(self, space):
        # If the cursor object line is in the last position
        if space[-1] == "^":
            # Then it does nothing
            return space

        # Takes the position of the cursor object line
        position = space.index("^")

        # Separates the cursor object line into its individual elements
        individual_characters = [char for char in space]

        # Changes that position with a space
        individual_characters[position] = " "

        # Adds the cursor object line to the space to the right
        individual_characters[position + 1] = "^"

        # Unites it once again
        space = "".join(individual_characters)

        # Returns the cursor object line
        return space

    def move_left(self, space):
        # If the cursor object line is in the first position
        if space[0] == "^":
            # Does nothing
            return space

        # Takes the position of the cursor object line
        position = space.index("^")

        # Separates the cursor object line into its individual elements
        individual_characters = [char for char in space]

        # Replaces this position with a space
        individual_characters[position] = " "

        # Replaces the position to the left with the cursor object
        individual_characters[position - 1] = "^"

        # Unites it once again
        space = "".join(individual_characters)

        # Returns the cursor object line
        return space

    def insert(self, phrase, space, character):
        # Takes the position to the right of the cursor object line
        position = space.index("^") + 1

        # Separates the phrase nto its individual elements
        individual_characters = [char for char in self._phrase]

        # Generates a list with the first nth elements
        new = individual_characters[0: position]

        # Generates a list with the remaining elements
        after = individual_characters[position:]

        # adds the new character
        new.append(character)

        # Adds again the remaining elements
        for i in after:
            new.append(i)

        # Unites it once again
        final = "".join(new)

        # Returns the new phrase
        return final

    def delete(self, phrase):
        # Takes the position to the right of the cursor object line
        position = self._space.index("^") + 1

        # Separated the elemetns of the phrase into a list
        individual_characters = [char for char in self._phrase]

        # Deletes the one that is in the position to the right of the cursor object line
        del individual_characters[position]

        # Units it once again
        final = "".join(individual_characters)

        # Returns the new phrase
        return final

