from lark import Lark
from lark.indenter import Indenter

# Custom Indenter class to handle indentation
class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

# Load the grammar from the file
with open('grammar/scratch.lark', 'r') as grammar_file:
    grammar = grammar_file.read()

# Load the input text from the file
with open('example/level1_model.uvl', 'r') as input_file:
    input_text = input_file.read()

# Create the parser with Earley for detailed error reporting
parser = Lark(grammar, parser='lalr', postlex=TreeIndenter(), debug=True)

# Parse the input
try:
    tree = parser.parse(input_text)
    print(tree.pretty())
except Exception as e:
    print(e)
