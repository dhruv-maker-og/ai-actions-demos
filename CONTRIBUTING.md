# Contributing to AI Actions Demos

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Issues

- Use the issue triage workflow to see how AI can help analyze issues
- Provide clear reproduction steps
- Include relevant environment details

### Submitting Changes

1. **Fork the repository**
   ```bash
   gh repo fork YOUR_USERNAME/ai-actions-demos
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Update documentation if needed
   - Test your changes

4. **Commit with clear messages**
   ```bash
   git commit -m "feat: add new demo workflow"
   ```

5. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   gh pr create
   ```

### Workflow Contributions

When adding new workflow demos:

1. Create workflow file in `.github/workflows/`
2. Use descriptive name: `demo#-short-description.yml`
3. Include comprehensive comments
4. Add documentation to README.md
5. Test the workflow in your fork first

### Prompt Engineering

If improving AI prompts:

1. Edit prompt files in `.github/prompts/` (for Demos 3-4)
2. Edit workflow YAML inline prompts (for Demos 1-2)
3. Test with various scenarios
4. Document prompt changes and rationale

### Code Style

- **YAML**: 2-space indentation
- **Shell**: Follow shellcheck recommendations
- **Python**: Follow PEP 8
- **Markdown**: Use consistent heading levels

### Testing

Before submitting:

1. Test workflow in your fork
2. Verify all steps complete successfully
3. Check logs for errors or warnings
4. Ensure permissions are minimal and correct

## Ideas for New Demos

We welcome ideas for new AI-powered workflow demos:

- [ ] Automated changelog generation
- [ ] Sentiment analysis on user feedback
- [ ] Multi-language issue translation
- [ ] Intelligent issue assignment
- [ ] PR complexity scoring and review suggestions
- [ ] Security vulnerability detection with AI
- [ ] Performance regression detection
- [ ] Automated test generation from code changes

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## Questions?

Open an issue with the `question` label and our AI triage will help!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for making this project better! 🚀
