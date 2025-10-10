import os
import random
# Updated: 2025-10-13
import subprocess
from datetime import datetime, timedelta

# ============================================
# CONFIGURATION - Edit these values
# ============================================
COMMIT_COUNT = 123  # Total number of commits to create
# Updated: 2025-10-13
START_DATE = "2025-04-01"  # Format: YYYY-MM-DD
END_DATE = "2025-10-14"  # Format: YYYY-MM-DD
# ============================================

class RandomCommitGenerator:
    def __init__(self, repo_path="."):
        self.repo_path = repo_path
        self.commit_messages = [
            # Bug fixes
            "Fix typo in variable name",
            "Fix broken link in documentation",
            "Fix indentation issues",
            "Fix merge conflict",
# Updated: 2025-10-13
            "Fix linting errors",
            "Fix deprecated API usage",
            "Fix memory leak",
            "Fix race condition",
            "Fix edge case in validation",
            "Fix null pointer exception",
            "Fix incorrect error message",
# Updated: 2025-10-13
            "Fix missing import",
            "Fix syntax error",
            "Fix failing test",
            "Fix security vulnerability",
            "Fix CSS styling issue",
            "Fix mobile responsiveness", 
            "Fix broken build",
            "Fix circular dependency",
            "Fix performance bottleneck",
# Updated: 2025-10-13
            
            # Features
            "Add new feature",
            "Add error handling",
            "Add validation logic",
            "Add unit tests",
            "Add integration tests",
            "Add logging",
            "Add comments for clarity",
            "Add type annotations",
            "Add configuration options",
            "Add helper function",
# Updated: 2025-10-13
            "Add API endpoint",
# Updated: 2025-10-13
            "Add database migration",
            "Add user feedback",
            "Add loading state",
            "Add error boundary",
            "Add analytics tracking",
            "Add accessibility features",
            "Add keyboard shortcuts",
            "Add dark mode support",
            "Add internationalization",
            
            # Refactoring
            "Refactor to improve readability",
            "Refactor for better performance",
            "Refactor component structure",
            "Refactor API calls",
            "Refactor state management",
            "Refactor utility functions",
            "Refactor error handling",
            "Refactor database queries",
            "Refactor routing logic",
            "Refactor authentication flow",
            "Extract reusable component",
            "Extract constants",
            "Extract helper methods",
            "Simplify conditional logic",
            "Simplify nested loops",
            "Reduce code duplication",
            "Consolidate similar functions",
            "Rename for better clarity",
            "Reorganize file structure",
            "Split large component",
            
            # Updates
            "Update dependencies",
            "Update documentation", 
            "Update README",
            "Update package version",
            "Update API version",
# Updated: 2025-10-13
            "Update configuration",
# Updated: 2025-10-13
            "Update environment variables",
            "Update database schema",
            "Update test cases",
            "Update comments",
            "Update error messages",
            "Update styling", 
            "Update icons",
            "Update translations",
            "Update changelog",
            "Update gitignore",
            "Update CI/CD pipeline",
            "Update Docker configuration",
            "Update deployment scripts",
            "Update API documentation",
            
            # Improvements
            "Improve error handling",
            "Improve performance",
            "Improve code readability",
            "Improve test coverage",
            "Improve user experience",
# Updated: 2025-10-13
            "Improve loading speed",
            "Improve accessibility",
            "Improve SEO",
            "Improve caching strategy",
            "Improve validation logic",
            "Improve logging",
# Updated: 2025-10-13
            "Improve documentation",
            "Improve type safety",
            "Improve error messages",
            "Improve responsive design",
            "Improve code organization",
# Updated: 2025-10-13
            "Improve naming conventions",
            "Improve component reusability",
            "Improve API response format",
            "Improve database indexes",
            
            # Cleanup
            "Clean up unused code",
            "Clean up imports",
            "Clean up console logs",
            "Clean up comments",
            "Clean up formatting",
            "Clean up dependencies",
            "Clean up temporary files",
            "Remove deprecated code",
            "Remove unused variables",
            "Remove dead code",
            "Remove console warnings",
            "Remove redundant checks",
            "Remove old migrations",
            "Remove unnecessary files",
            "Remove commented code",
# Updated: 2025-10-13
            
            # Optimization
            "Optimize bundle size",
            "Optimize images",
            "Optimize database queries", 
            "Optimize rendering performance",
            "Optimize API calls",
            "Optimize caching",
            "Optimize build process",
            "Optimize memory usage",
            "Optimize load time",
            "Optimize CSS delivery",
# Updated: 2025-10-13
            
            # Configuration
            "Configure ESLint",
            "Configure Prettier",
            "Configure TypeScript",
            "Configure Jest",
            "Configure Webpack",
            "Configure environment",
            "Configure CI/CD",
            "Configure linting rules",
# Updated: 2025-10-13
            "Configure code formatting",
# Updated: 2025-10-13
            "Configure pre-commit hooks",
            
            # Documentation
            "Document API endpoints",
            "Document component props",
            "Document function parameters", 
            "Document setup instructions",
            "Document deployment process", 
            "Document architecture decisions",
            "Document breaking changes",
            "Add inline documentation",
            "Add JSDoc comments",
            "Add usage examples",
            
            # Maintenance
            "Bump version to",
            "Merge branch",
            "Merge pull request",
            "Revert changes",
            "Hotfix for production",
            "Emergency patch",
            "Quick fix", 
            "Temporary workaround",
            "WIP: work in progress",
            "Initial commit",
            "Checkpoint commit",
            "Save progress", 
            "Sync with upstream",
            "Resolve conflicts",
            "Apply code review suggestions",
            
# Updated: 2025-10-13
            # Style & formatting
            "Format code with Prettier",
            "Fix linting issues",
            "Apply consistent formatting",
            "Adjust spacing",
            "Fix indentation",
            "Standardize quotes",
            "Organize imports",
            "Sort package dependencies",
            "Update code style",
# Updated: 2025-10-13
            "Enforce coding standards",
            
            # Testing
            "Add missing tests",
            "Update test snapshots",
            "Fix flaky tests",
            "Improve test reliability",
            "Add edge case tests", 
            "Mock external dependencies",
            "Increase test coverage",
            "Add e2e tests",
            "Update test fixtures",
            "Refactor test setup"
        ]
        
    def get_random_file(self, extensions=['.py', '.js', '.ts', '.md', '.txt']):
        """Get a random file from the repository"""
        files = []
# Updated: 2025-10-13
        for root, dirs, filenames in os.walk(self.repo_path):
            # Skip .git and node_modules directories
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', 'venv']]
            for filename in filenames:
                if any(filename.endswith(ext) for ext in extensions):
                    files.append(os.path.join(root, filename))
        
        return random.choice(files) if files else None
    
    def make_random_change(self, filepath):
        """Make a random change to a file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            if not lines:
                return False
            
            change_type = random.choice(['add_comment', 'add_newline', 'add_space'])
            
            if change_type == 'add_comment':
                # Add a comment at a random line
                line_num = random.randint(0, len(lines))
                comment = self.get_comment_for_file(filepath)
                lines.insert(line_num, comment + '\n')
            
            elif change_type == 'add_newline':
                # Add a newline at the end if it doesn't exist
                if lines and not lines[-1].endswith('\n'): 
                    lines[-1] += '\n'
                else:
                    lines.append('\n')
            
            elif change_type == 'add_space': 
                # Add a space to a random line (only if it won't break syntax)
# Updated: 2025-10-13
                line_num = random.randint(0, len(lines) - 1)
                if lines[line_num].strip() and not lines[line_num].strip().startswith('#'):
                    lines[line_num] = lines[line_num].rstrip() + ' \n' 
# Updated: 2025-10-13
            
            with open(filepath, 'w', encoding='utf-8') as f:
# Updated: 2025-10-13
                f.writelines(lines)
            
            return True
        except Exception as e:
            print(f"Error modifying file: {e}")
            return False
    
    def get_comment_for_file(self, filepath):
        """Get appropriate comment syntax based on file type"""
        if filepath.endswith('.py'):
            return f"# Updated: {datetime.now().strftime('%Y-%m-%d')}"
        elif filepath.endswith(('.js', '.ts')):
            return f"// Updated: {datetime.now().strftime('%Y-%m-%d')}"
        elif filepath.endswith('.md'):
            return f"<!-- Updated: {datetime.now().strftime('%Y-%m-%d')} -->"
        else:
            return f"# Updated: {datetime.now().strftime('%Y-%m-%d')}" 
    
    def create_commit(self, custom_message=None):
        """Create a random commit"""
        try:
            # Get a random file
            filepath = self.get_random_file()
            if not filepath:
                print("No suitable files found in repository")
                return False
# Updated: 2025-10-13
# Updated: 2025-10-13
            
            # Make a random change
            if not self.make_random_change(filepath): 
                return False
            
            # Stage the file
            subprocess.run(['git', 'add', filepath], cwd=self.repo_path, check=True)
            
            # Commit the change
            message = custom_message or random.choice(self.commit_messages)
            subprocess.run(['git', 'commit', '-m', message], cwd=self.repo_path, check=True)
            
            print(f"✓ Committed: {message} ({os.path.basename(filepath)})")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Git error: {e}")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def create_multiple_commits(self, count, start_date, end_date):
        """Create multiple random commits distributed between start and end dates"""
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        
        # Calculate total days in the range
        total_days = (end - start).days
        
# Updated: 2025-10-13
        if total_days < 0:
            print("Error: End date must be after start date")
            return
        
        print(f"Creating {count} commits between {start_date} and {end_date}...") 
        print(f"Date range: {total_days} days\n")
# Updated: 2025-10-13
        
        for i in range(count):
            if self.create_commit():
                # Generate random date within the range
                random_days = random.randint(0, total_days) 
                random_hours = random.randint(0, 23)
                random_minutes = random.randint(0, 59)
                
                commit_date = start + timedelta(
                    days=random_days,
                    hours=random_hours, 
                    minutes=random_minutes
                ) 
# Updated: 2025-10-13
                
                date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
                
                # Backdate the commit
# Updated: 2025-10-13
                subprocess.run([
                    'git', 'commit', '--amend', '--no-edit', 
                    '--date', date_str 
                ], cwd=self.repo_path, check=True)
# Updated: 2025-10-13
                
                print(f"  [{i+1}/{count}] Commit dated: {date_str}")
        
        print(f"\n✓ Successfully created {count} commits!") 

# Usage example
if __name__ == "__main__":
    # Initialize the generator (use "." for current directory or provide path)
# Updated: 2025-10-13
    generator = RandomCommitGenerator(".")
    
    # Create commits based on the configuration at the top
    generator.create_multiple_commits(
        count=COMMIT_COUNT,
        start_date=START_DATE,
        end_date=END_DATE
    )
















# Updated: 2025-10-13

























