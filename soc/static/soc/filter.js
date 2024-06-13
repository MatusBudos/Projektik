function filterThemes() {
  const filterAvailability = document.getElementById('filter-select').value;
  const filterOdbor = document.getElementById('filter-odbor').value;
  const filterKonzultant = document.getElementById('filter-konzultant').value;
  const temaItems = document.querySelectorAll('.tema-item');

  temaItems.forEach(item => {
    const dostupnost = item.getAttribute('data-dostupnost');
    const odbor = item.getAttribute('data-odbor');
    const konzultant = item.getAttribute('data-konzultant');

    let showItem = true;

    if (filterAvailability !== 'all' && dostupnost !== filterAvailability) {
      showItem = false;
    }

    if (filterOdbor !== 'all' && odbor !== filterOdbor) {
      showItem = false;
    }

    if (filterKonzultant !== 'all' && konzultant !== filterKonzultant) {
      showItem = false;
    }

    if (showItem) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }

    item.querySelector('.dostupnost-label').classList.remove('volne', 'cakajuce', 'obsadene');

    switch (parseInt(dostupnost)) {
      case 1:
        item.querySelector('.dostupnost-label').classList.add('volne');
        break;
      case 2:
        item.querySelector('.dostupnost-label').classList.add('cakajuce');
        break;
      case 3:
        item.querySelector('.dostupnost-label').classList.add('obsadene');
        break;
      default:
        break;
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  filterThemes();
});