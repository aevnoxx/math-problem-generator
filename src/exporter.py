"""
Export functionality for math problems
Supports Markdown and LaTeX formats
"""

from typing import List, Dict
from datetime import datetime


class ProblemExporter:
    """Export problems to various formats"""

    @staticmethod
    def to_markdown(problems: List[Dict], title: str = "Math Problem Set") -> str:
        """
        Export problems to Markdown format

        Args:
            problems: List of problem dictionaries
            title: Title for the problem set

        Returns:
            Markdown formatted string
        """
        md = f"# {title}\n\n"
        md += f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"
        md += "---\n\n"

        for problem in problems:
            md += f"## Problem {problem['number']}\n\n"
            md += f"**Type:** {problem['type'].capitalize()}  \n"
            md += f"**Difficulty:** {problem['difficulty'].capitalize()}  \n\n"

            if problem["type"] == "derivative":
                md += f"Find the derivative of:\n\n"
                md += f"$$f(x) = {problem['function_latex']}$$\n\n"
            elif problem["type"] == "integral":
                md += f"Find the integral of:\n\n"
                md += f"$$\\int {problem['function_latex']} \\, dx$$\n\n"
            else:  # limit
                md += f"Find the limit:\n\n"
                md += f"$$\\lim_{{x \\to {problem['point']}}} {problem['function_latex']}$$\n\n"

            md += "### Solution\n\n"
            md += f"$$" + problem["solution_latex"] + "$$\n\n"

            if "steps" in problem and problem["steps"]:
                md += "### Steps\n\n"
                for step in problem["steps"]:
                    md += f"- {step}\n"
                md += "\n"

            md += "---\n\n"

        return md

    @staticmethod
    def to_latex(problems: List[Dict], title: str = "Math Problem Set") -> str:
        """
        Export problems to LaTeX format

        Args:
            problems: List of problem dictionaries
            title: Title for the problem set

        Returns:
            LaTeX formatted string
        """
        latex = (
            r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}

\title{"""
            + title
            + r"""}
\author{Math Problem Generator}
\date{"""
            + datetime.now().strftime("%Y-%m-%d")
            + r"""}

\begin{document}

\maketitle

"""
        )

        for problem in problems:
            latex += f"\\section*{{Problem {problem['number']}}}\n\n"
            latex += f"\\textbf{{Type:}} {problem['type'].capitalize()} \\\\\n"
            latex += f"\\textbf{{Difficulty:}} {problem['difficulty'].capitalize()}\n\n"

            if problem["type"] == "derivative":
                latex += "Find the derivative of:\n\n"
                latex += f"$$f(x) = {problem['function_latex']}$$\n\n"
            elif problem["type"] == "integral":
                latex += "Find the integral of:\n\n"
                latex += f"$$\\int {problem['function_latex']} \\, dx$$\n\n"
            else:  # limit
                latex += "Find the limit:\n\n"
                latex += f"$$\\lim_{{x \\to {problem['point']}}} {problem['function_latex']}$$\n\n"

            latex += "\\subsection*{Solution}\n\n"
            latex += f"$${problem['solution_latex']}$$\n\n"

            if "steps" in problem and problem["steps"]:
                latex += "\\subsection*{Steps}\n\n"
                latex += "\\begin{enumerate}\n"
                for step in problem["steps"]:
                    latex += f"    \\item {step}\n"
                latex += "\\end{enumerate}\n\n"

            latex += "\\vspace{1cm}\n\n"

        latex += r"""
\end{document}
"""
        return latex

    @staticmethod
    def to_text(problems: List[Dict]) -> str:
        """
        Export problems to plain text format

        Args:
            problems: List of problem dictionaries

        Returns:
            Plain text formatted string
        """
        text = f"Math Problem Set\n"
        text += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        text += "=" * 50 + "\n\n"

        for problem in problems:
            text += f"Problem {problem['number']}\n"
            text += f"Type: {problem['type'].capitalize()}\n"
            text += f"Difficulty: {problem['difficulty'].capitalize()}\n"
            text += "-" * 50 + "\n"
            text += f"Function: {problem['function']}\n"
            text += f"Solution: {problem['solution']}\n\n"

            if "steps" in problem and problem["steps"]:
                text += "Steps:\n"
                for i, step in enumerate(problem["steps"], 1):
                    text += f"{i}. {step}\n"

            text += "\n" + "=" * 50 + "\n\n"

        return text
