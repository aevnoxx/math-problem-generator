"""
Usage Examples for Math Problem Generator
Demonstrates various ways to use the library programmatically
"""

from src.generator import ProblemGenerator
from src.exporter import ProblemExporter


def example_basic_usage():
    """Basic usage - generate and print problems"""
    print("=== Example 1: Basic Usage ===\n")
    
    generator = ProblemGenerator()
    
    # Generate a single derivative problem
    problem = generator.generate_derivative_problem(difficulty='easy')
    
    print(f"Problem Type: {problem['type']}")
    print(f"Function: {problem['function']}")
    print(f"Solution: {problem['solution']}")
    print()


def example_custom_problem_set():
    """Generate a custom problem set"""
    print("=== Example 2: Custom Problem Set ===\n")
    
    generator = ProblemGenerator(seed=42)  # Use seed for reproducibility
    
    # Generate 5 derivative problems
    problems = generator.generate_problem_set(
        count=5,
        problem_types=['derivative'],
        difficulty='medium'
    )
    
    for prob in problems:
        print(f"Problem {prob['number']}: {prob['function']}")
    print()


def example_export_formats():
    """Export problems to different formats"""
    print("=== Example 3: Export to Multiple Formats ===\n")
    
    generator = ProblemGenerator(seed=123)
    problems = generator.generate_problem_set(count=3)
    
    exporter = ProblemExporter()
    
    # Export to Markdown
    md_output = exporter.to_markdown(problems, title="Practice Problems")
    print("Markdown output length:", len(md_output), "characters")
    
    # Export to LaTeX
    latex_output = exporter.to_latex(problems, title="Homework Set")
    print("LaTeX output length:", len(latex_output), "characters")
    
    # Export to plain text
    text_output = exporter.to_text(problems)
    print("Text output length:", len(text_output), "characters")
    print()


def example_specific_problem_types():
    """Generate specific types of problems"""
    print("=== Example 4: Specific Problem Types ===\n")
    
    generator = ProblemGenerator()
    
    # Only derivatives
    derivative = generator.generate_derivative_problem(difficulty='hard')
    print(f"Derivative: f(x) = {derivative['function']}")
    print(f"Solution: f'(x) = {derivative['solution']}\n")
    
    # Only integrals
    integral = generator.generate_integral_problem(difficulty='medium')
    print(f"Integral: ∫ {integral['function']} dx")
    print(f"Solution: {integral['solution']}\n")
    
    # Only limits
    limit = generator.generate_limit_problem(difficulty='hard')
    print(f"Limit: lim(x→{limit['point']}) {limit['function']}")
    print(f"Solution: {limit['solution']}\n")


def example_batch_generation():
    """Generate multiple problem sets"""
    print("=== Example 5: Batch Generation ===\n")
    
    difficulties = ['easy', 'medium', 'hard']
    
    for difficulty in difficulties:
        generator = ProblemGenerator()
        problems = generator.generate_problem_set(
            count=3,
            difficulty=difficulty
        )
        print(f"{difficulty.capitalize()} problems: {len(problems)} generated")
    print()


def example_with_steps():
    """Show problem with solution steps"""
    print("=== Example 6: Problem with Solution Steps ===\n")
    
    generator = ProblemGenerator(seed=999)
    problem = generator.generate_derivative_problem(difficulty='medium')
    
    print(f"Function: {problem['function']}")
    print(f"Solution: {problem['solution']}\n")
    print("Steps:")
    for i, step in enumerate(problem['steps'], 1):
        print(f"  {i}. {step}")
    print()


def example_save_to_file():
    """Generate and save to file"""
    print("=== Example 7: Save to File ===\n")
    
    from pathlib import Path
    
    generator = ProblemGenerator()
    problems = generator.generate_problem_set(count=5, difficulty='medium')
    
    exporter = ProblemExporter()
    
    # Save as Markdown
    md_content = exporter.to_markdown(problems, title="Weekly Homework")
    Path("examples/example_homework.md").write_text(md_content)
    print("✓ Saved to examples/example_homework.md")
    
    # Save as LaTeX
    latex_content = exporter.to_latex(problems, title="Weekly Homework")
    Path("examples/example_homework.tex").write_text(latex_content)
    print("✓ Saved to examples/example_homework.tex")
    print()


if __name__ == "__main__":
    print("Math Problem Generator - Usage Examples\n")
    print("=" * 60)
    print()
    
    example_basic_usage()
    example_custom_problem_set()
    example_export_formats()
    example_specific_problem_types()
    example_batch_generation()
    example_with_steps()
    example_save_to_file()
    
    print("=" * 60)
    print("\nAll examples completed successfully!")
