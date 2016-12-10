// modified from http://callmenick.com/post/animated-resizing-header-on-scroll
function hasClass(el, className) {
  if (el.classList)
    return el.classList.contains(className)
  else
    return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'))
}

function addClass(el, className) {
  if (el.classList)
    el.classList.add(className)
  else if (!hasClass(el, className)) el.className += " " + className
}

function removeClass(el, className) {
  if (el.classList)
    el.classList.remove(className)
  else if (hasClass(el, className)) {
    var reg = new RegExp('(\\s|^)' + className + '(\\s|$)')
    el.className=el.className.replace(reg, ' ')
  }
}


function init() {
    window.addEventListener('scroll', function(e){
        var distanceY = window.pageYOffset || document.documentElement.scrollTop,
            shrinkOn = 150,
            seal = document.getElementsByClassName("s")[0];;
        if (distanceY > shrinkOn) {
            addClass(seal,"s--u");
        } else {
            if (hasClass(seal,"s--u")) {
                removeClass(seal,"s--u");
            }
        }
    });
}
window.onload = init();
