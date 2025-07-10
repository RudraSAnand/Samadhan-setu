const form = document.getElementById('grievanceForm');
const progress = document.getElementById('formProgress');
const modal = document.getElementById('confirmModal');

function getFilledFields() {
  if (!form) return 0;
  let count = 0;
  ['name','email','phone','category','title','description'].forEach(id => {
    if (document.getElementById(id) && document.getElementById(id).value.trim()) count++;
  });
  return count;
}

function updateProgress() {
  if (progress) progress.style.width = (getFilledFields() / 6 * 100) + '%';
}

if (form) {
  form.addEventListener('input', updateProgress);

  document.getElementById('autoLocation').onclick = function(e) {
    if (!navigator.geolocation) return alert('Geolocation not supported');
    navigator.geolocation.getCurrentPosition(function(pos) {
      document.getElementById('location').value = `Lat: ${pos.coords.latitude.toFixed(4)}, Lon: ${pos.coords.longitude.toFixed(4)}`;
      updateProgress();
    }, function(err) {
      alert('Unable to fetch your location.');
    });
  };

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    let ok = true;
    ['name','email','phone','category','title','description'].forEach(function(id) {
      const el = document.getElementById(id);
      if (!el.value.trim()) {
        el.style.borderColor = 'var(--saffron)';
        ok = false;
      } else {
        el.style.borderColor = '#ddd';
      }
    });
    if (!ok) return;
    if (modal) {
      modal.classList.add('active');
      form.reset();
      updateProgress();
    }
  });
}
window.addEventListener('keydown', function(evt) {
  if ((evt.key === 'Escape' || evt.key === 'Esc') && modal) {
    modal.classList.remove('active');
  }
});

