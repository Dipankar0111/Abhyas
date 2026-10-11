import subprocess
import time

# We can launch Chrome with a small script in the console or just inspect via Chrome
html_with_test_active = """
<!DOCTYPE html>
<html>
<head>
<script>
window.addEventListener('DOMContentLoaded', () => {
  // simulate clicking start test
  setTimeout(() => {
    window.selectAndLaunchBatch(0);
    setTimeout(() => {
      window.confirmLaunchTest();
    }, 200);
  }, 300);
});
</script>
</head>
<body>
</body>
</html>
"""

# Or better yet, we can evaluate a script via Chrome remote debugging or create a test_runner page
