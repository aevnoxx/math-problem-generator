"""
Command-line interface for Math Problem Generator
"""

import argparse
import json
from pathlib import Path
from src.generator import ProblemGenerator
from src.exporter import ProblemExporter


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Generate mathematical problems with solutions"
    )

    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=5,
        help="Number of problems to generate (default: 5)",
    )

    parser.add_argument(
        "-d",
        "--difficulty",
        choices=["easy", "medium", "hard"],
        default="medium",
        help="Difficulty level (default: medium)",
    )

    parser.add_argument(
        "-t",
        "--types",
        nargs="+",
        choices=["derivative", "integral", "limit"],
        default=["derivative", "integral", "limit"],
        help="Problem types to generate",
    )

    parser.add_argument(
        "-f",
        "--format",
        choices=["markdown", "latex", "text", "json"],
        default="markdown",
        help="Output format (default: markdown)",
    )

    parser.add_argument("-o", "--output", type=str, help="Output file path (optional)")

    parser.add_argument(
        "-s", "--seed", type=int, help="Random seed for reproducibility (optional)"
    )

    parser.add_argument(
        "--title",
        type=str,
        default="Math Problem Set",
        help="Title for the problem set",
    )

    args = parser.parse_args()

    # Generate problems
    generator = ProblemGenerator(seed=args.seed)
    problems = generator.generate_problem_set(
        count=args.count, problem_types=args.types, difficulty=args.difficulty
    )

    # Export to chosen format
    exporter = ProblemExporter()

    if args.format == "markdown":
        output = exporter.to_markdown(problems, title=args.title)
        extension = ".md"
    elif args.format == "latex":
        output = exporter.to_latex(problems, title=args.title)
        extension = ".tex"
    elif args.format == "text":
        output = exporter.to_text(problems)
        extension = ".txt"
    else:  # json
        output = json.dumps(problems, indent=2, ensure_ascii=False)
        extension = ".json"

    # Output to file or stdout
    if args.output:
        output_path = Path(args.output)
        # Add extension if not present
        if not output_path.suffix:
            output_path = output_path.with_suffix(extension)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output, encoding="utf-8")
        print(f"✓ Generated {args.count} problems")
        print(f"✓ Saved to: {output_path}")
    else:
        print(output)


if __name__ == "__main__":
    main()
