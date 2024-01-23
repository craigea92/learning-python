"""
SCOPE QUIZ

Local Scope
Variables declared inside functions
Limited to the function where they are created

Global Scope
Variables declared outside any function, within the module
Accessible inside and outside functions

The LEGB Rule

Is a set of guidelines in Python that defines the order in which the interpreter looks for variable names during name resolution.
The acronym stands for:

Local (L): The innermost scope, which is the current function or block where the variable is defined

Enclosed (E): Any enclosing scopes. This applies to nested functions

Global (G): The module-level scope. Variables defined at the top level of a script or module

Built-in (B): The outermost scope, which includes built-in names like `print`, `len`, etc
"""

# Question 01

# Can functions access variables declared in the global scope?

# Yes
# No

# Answer = Yes

# Question 02

# Can code outside the scope of a function access variables that are inside that function?

# Yes
# No

# Answer = No