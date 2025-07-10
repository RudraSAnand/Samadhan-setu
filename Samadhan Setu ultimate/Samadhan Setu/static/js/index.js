function animateCounter(id, endValue, duration) {
  const el = document.getElementById(id);
  if (!el) return;
  let start = 0;
  const increment = Math.ceil(endValue / (duration / 20));
  const timer = setInterval(() => {
    start += increment;
    if (start >= endValue) {
      el.textContent = endValue.toLocaleString('en-IN');
      clearInterval(timer);
    } else {
      el.textContent = start.toLocaleString('en-IN');
    }
  }, 20);
}

document.addEventListener('DOMContentLoaded', function() {
  animateCounter('complaintsResolved', 8, 1300);
  animateCounter('citizensServed', 10, 1700);
  animateCounter('departmentsOnboarded', 7, 1200);
});
