document.getElementById("clearFilters").addEventListener("click", function() {
  document.getElementById("minSalary").value = '';
  document.getElementById("maxSalary").value = '';
  document.getElementById("postedAfter").value = '';
  document.getElementById("postedBefore").value = '';
  document.getElementById("jobTypeFilter").selectedIndex = 0;
  document.getElementById("filterForm").submit(); // Submit the form after clearing the fields
});