window.smoothScroll = function(target) {
    var scrollContainer = target;
    do { //find scroll container
        scrollContainer = scrollContainer.parentNode;
        if (!scrollContainer) return;
        scrollContainer.scrollTop += 1;
    } while (scrollContainer.scrollTop == 0);

    var targetY = 0;
    do { //find the top of target relatively to the container
        if (target == scrollContainer) break;
        targetY += target.offsetTop;
    } while (target = target.offsetParent);

    scroll = function(c, a, b, i) {
        i++; if (i > 30) return;
        c.scrollTop = a + (b - a) / 30 * i;
        setTimeout(function(){ scroll(c, a, b, i); }, 20);
    }
    // start scrolling
    scroll(scrollContainer, scrollContainer.scrollTop, targetY, 0);
}

let searchExam = document.getElementById('searchExam');

searchExam.addEventListener('input', () => {
    let inputText = searchExam.value.toLowerCase();
    let examCard = document.getElementsByClassName('card');
    Array.from(examCard).forEach(element => {
        let exam_title = element.getElementsByTagName('h3')[0];
        let title = exam_title.innerText.toLowerCase();
        if (title.includes(inputText)) {
            element.style.display = "block";
        }
        else {
            element.style.display = "none";
        }
    })
})
