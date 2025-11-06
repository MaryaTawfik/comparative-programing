class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_code = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        
        # Map each letter to its Morse code
        letter_to_morse = {chr(i + ord('a')): code for i, code in enumerate(morse_code)}
        
        # Use a set to store unique transformations
        transformations = set()
        
        for word in words:
            transformation = ''.join(letter_to_morse[char] for char in word)
            transformations.add(transformation)
        
        return len(transformations)
