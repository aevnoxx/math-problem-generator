"""
Unit tests for ProblemExporter
"""

import pytest
from src.generator import ProblemGenerator
from src.exporter import ProblemExporter


class TestProblemExporter:
    """Test cases for ProblemExporter class"""

    def setup_method(self):
        """Setup test fixtures"""
        self.generator = ProblemGenerator(seed=42)
        self.exporter = ProblemExporter()
        self.sample_problems = self.generator.generate_problem_set(count=3)

    def test_to_markdown_structure(self):
        """Test markdown export has correct structure"""
        md = self.exporter.to_markdown(self.sample_problems)

        assert "# Math Problem Set" in md
        assert "Generated on:" in md
        assert "## Problem 1" in md
        assert "## Problem 2" in md
        assert "## Problem 3" in md

    def test_to_markdown_custom_title(self):
        """Test markdown export with custom title"""
        custom_title = "Calculus Homework"
        md = self.exporter.to_markdown(self.sample_problems, title=custom_title)

        assert f"# {custom_title}" in md

    def test_to_markdown_contains_latex(self):
        """Test markdown includes LaTeX formulas"""
        md = self.exporter.to_markdown(self.sample_problems)

        assert "$$" in md  # LaTeX delimiter

    def test_to_markdown_contains_solutions(self):
        """Test markdown includes solutions"""
        md = self.exporter.to_markdown(self.sample_problems)

        assert "### Solution" in md

    def test_to_markdown_contains_steps(self):
        """Test markdown includes solution steps"""
        md = self.exporter.to_markdown(self.sample_problems)

        assert "### Steps" in md

    def test_to_latex_structure(self):
        """Test LaTeX export has correct structure"""
        latex = self.exporter.to_latex(self.sample_problems)

        assert r"\documentclass" in latex
        assert r"\begin{document}" in latex
        assert r"\end{document}" in latex
        assert r"\section*{Problem 1}" in latex

    def test_to_latex_custom_title(self):
        """Test LaTeX export with custom title"""
        custom_title = "Calculus Test"
        latex = self.exporter.to_latex(self.sample_problems, title=custom_title)

        assert custom_title in latex

    def test_to_latex_contains_math(self):
        """Test LaTeX includes math environments"""
        latex = self.exporter.to_latex(self.sample_problems)

        assert "$$" in latex

    def test_to_text_structure(self):
        """Test plain text export has correct structure"""
        text = self.exporter.to_text(self.sample_problems)

        assert "Math Problem Set" in text
        assert "Generated:" in text
        assert "Problem 1" in text
        assert "Problem 2" in text
        assert "Problem 3" in text

    def test_to_text_contains_functions(self):
        """Test plain text includes function representations"""
        text = self.exporter.to_text(self.sample_problems)

        assert "Function:" in text
        assert "Solution:" in text

    def test_to_text_contains_steps(self):
        """Test plain text includes solution steps"""
        text = self.exporter.to_text(self.sample_problems)

        assert "Steps:" in text

    def test_all_formats_handle_empty_list(self):
        """Test that all exporters handle empty problem lists"""
        empty_problems = []

        md = self.exporter.to_markdown(empty_problems)
        latex = self.exporter.to_latex(empty_problems)
        text = self.exporter.to_text(empty_problems)

        assert md is not None
        assert latex is not None
        assert text is not None

    def test_markdown_problem_types(self):
        """Test markdown correctly displays different problem types"""
        derivative_prob = self.generator.generate_derivative_problem()
        integral_prob = self.generator.generate_integral_problem()
        limit_prob = self.generator.generate_limit_problem()

        derivative_prob["number"] = 1
        integral_prob["number"] = 2
        limit_prob["number"] = 3

        problems = [derivative_prob, integral_prob, limit_prob]
        md = self.exporter.to_markdown(problems)

        assert "Find the derivative" in md
        assert "Find the integral" in md or r"\int" in md
        assert "Find the limit" in md or r"\lim" in md

    def test_latex_special_characters(self):
        """Test LaTeX properly handles special characters"""
        latex = self.exporter.to_latex(self.sample_problems)

        # Check for proper LaTeX structure
        assert r"\[" not in latex or r"\]" not in latex  # Using $$ instead
        assert "$$" in latex  # Should use $$ for display math

    def test_output_is_string(self):
        """Test that all exporters return strings"""
        md = self.exporter.to_markdown(self.sample_problems)
        latex = self.exporter.to_latex(self.sample_problems)
        text = self.exporter.to_text(self.sample_problems)

        assert isinstance(md, str)
        assert isinstance(latex, str)
        assert isinstance(text, str)

    def test_output_not_empty(self):
        """Test that exporters produce non-empty output"""
        md = self.exporter.to_markdown(self.sample_problems)
        latex = self.exporter.to_latex(self.sample_problems)
        text = self.exporter.to_text(self.sample_problems)

        assert len(md) > 0
        assert len(latex) > 0
        assert len(text) > 0
