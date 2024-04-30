let [seconds, minutes, hours] = [0, 0, 0];
let displayTime = document.getElementById("displayTime");
let displayTime2 = document.getElementById("displayTime2");
let timer = null;
let pause = document.getElementById("pause");
let resume = document.getElementById("resume");

function stopWatch() {
    seconds++;
    if (seconds == 60) {
        seconds = 0;
        minutes++;
        if (minutes == 60) {
            minutes = 0;
            hours++;
        }
    }
    let h = hours < 10 ? "0" + hours : hours;
    let m = minutes < 10 ? "0" + minutes : minutes;
    let s = seconds < 10 ? "0" + seconds : seconds;

    displayTime.innerHTML = h + ":" + m + ":" + s;
    displayTime2.innerHTML = h + ":" + m + ":" + s;
}

function watchStart() {
    if (timer !== null) {
        clearInterval(timer);
    }
    timer = setInterval(stopWatch, 1000);
    pause.style.display = 'initial';
    resume.style.display = 'none';
}

function watchStop() {
    clearInterval(timer);
    resume.style.display = 'initial';
    pause.style.display = 'none';
}

function watchReset() {
    clearInterval(timer);
    [seconds, minutes, hours] = [0, 0, 0];
    displayTime.innerHTML = "00:00:00";
    resume.style.display = 'initial';
    pause.style.display = 'none';
}

watchStart();
