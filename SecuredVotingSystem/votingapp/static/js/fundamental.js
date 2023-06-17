$(document).ready(function() {
  $(document).on("contextmenu", function(e) {
    e.preventDefault();
    alert("Right-click context menu is disabled.");
  });

  $(document).keydown(function(e) {
    if (e.keyCode == 85 && (e.ctrlKey || e.metaKey)) {
      e.preventDefault();
      alert("View Source is disabled.");
    }
  });
});