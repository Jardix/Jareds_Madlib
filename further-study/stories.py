"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""
        
        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "History",
    "A Historic Tale!",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, long ago, in the lands of {place}, there lived a {noun}. This was no ordinary {noun}, but a {adjective} {noun}. And to pass its time, this {noun} loved nothing more than to simply {verb} absolutely every {plural_noun}, violently."""
)

story2 = Story(
    "Sci-Fi",
    "A tale from space!",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Long ago, in a star-system on the other side of the galaxy, lay the planet {place}...
    Ethan, the {noun}, surveyed the {adjective} landscape with a set of binoculars. Behind him, the smoldering wreck of his ship lie smoking, a horde of {plural_noun} already descending. Once their curiosity and fear had passed, they would no doubt try to {verb} poor Ethan to death."""
)

stories = {s.code: s for s in [story1, story2]}
