
function throttle(fn, delay) {
    let time = Date.now();
    return function () {
        if ((time + delay - Date.now()) < 0) {
            fn(arguments);
            time = Date.now();
        }
    }
}

function debounced(fn, delay) {
    let timerId;
    return function () {
        if (timerId) {
            clearTimeout(timerId);
        }
        timerId = setTimeout(() => {
            fn(arguments);
            timerId = null;
        }, delay);
    }
}

export {throttle, debounced};
