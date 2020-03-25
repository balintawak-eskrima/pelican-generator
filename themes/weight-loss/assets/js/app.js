require('../scss/app.scss');

const helpers = require('./helpers');

(function() {
    let elem = document.querySelector('.header');
    let classFeature = 'header-on-scroll';

    function setScroll(elem) {
        if(!elem.classList.contains(classFeature)) {
            elem.classList.add(classFeature);
        }
        return true;
    }

    function unsetScroll(elem) {
        if(elem.classList.contains(classFeature)) {
            elem.classList.remove(classFeature);
        }
        return true;
    }

    function isWidthAbove1024() {
        return window.innerWidth > 1024;
    }

    function isOnTop () {
        return (window.scrollY || document.documentElement.scrollTop) === 0;
    }

    function switchScroll() {
        isWidthAbove1024()
        && (isOnTop() && unsetScroll(elem) || setScroll(elem))
        || unsetScroll(elem);
    }

    let switchScrollHandler = helpers.debounced(function(e) { switchScroll()}, 10);

    window.addEventListener('load', function(e) {
        switchScroll();
        window.addEventListener('scroll', switchScrollHandler);
        window.addEventListener('resize', switchScrollHandler);
    });
})();






