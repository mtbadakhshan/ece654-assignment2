Assignment 2 Instructions


Code analysis on Control Flow Graph:

- Pick a programming language

- Pick a library to produce the CFG for a program

- Perform a simple even/odd analysis:

	- Devise a lattice that allows you to track the parity of values
	- Devise abstract operations to model primitive operations, at least for addition and multiplication
	- For every use of a variable, output the information collected; think of a suitable way to present the analysis results


Submit a report that contains:

- A link to your source repository
- Links to CI executions of your test cases
- Any observations about the used CFG library/tool
- A high-level description of how you implemented the analysis, including:
	- a description of the lattice,
	- whether it is a forward/backwards and may/must analysis, and
	- definitions for the abstract operations
	- Could this analysis be implemented on the AST instead? What are the trade-offs of an AST vs CFG based analysis? Explain using examples.
	- Can you think of further refinements to the lattice or a combination with other analyses that would improve this even/odd analysis?
	- Can this analysis have false positives or false negatives? What do these terms mean in this case?

General comments:

- Have a git repository with history
- Have a CI system set up
- Include test cases
	- Tests that show true positives
	- Tests that show true negatives
	- If applicable, false positives and false negatives
- Execute these tests in CI