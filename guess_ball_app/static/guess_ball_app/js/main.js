Date.prototype.addHours = function(h) {
  this.setTime(this.getTime() + (h * 60 * 60 * 1000));
  return this;
}

initTimers();
setOnCompetitionImageClickHandle();
initTicketList();

function initTimers() {

    if (document.getElementById("monthly_time") != null) {
        initCountdownTimer("monthly_time", new Date().addHours(24 * 11.1).getTime());
    }

    if (document.getElementById("weekly_time") != null) {
        initCountdownTimer("weekly_time", new Date().addHours(24 * 3.1).getTime());
    }

    if (document.getElementById("daily_time") != null) {
        initCountdownTimer("daily_time", new Date().addHours(0.01).getTime());
    }
}

function initCountdownTimer(obj_id, countdownDate) {

// Update the count down every 1 second
    var x = setInterval(() => {

        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = countdownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="demo"
        document.getElementById(obj_id).innerHTML = days + "d " + hours + "h "
            + minutes + "m " + seconds + "s ";

        // If the count down is finished, write some text
        if (distance < 0) {
            clearInterval(x);
            document.getElementById(obj_id).innerHTML = "EXPIRED";
        }
    }, 1000);
}

function setOnCompetitionImageClickHandle() {
    window.onload = () => {
        let competitionImage = document.getElementById("competition_image");
        if (competitionImage != null) {
            competitionImage.addEventListener("click", (e) => {
                console.log("lckjsad");
                updateEntryInputs(e.offsetX, e.offsetY);
            });
        }
    };
}

function updateEntryInputs(offsetX, offsetY) {
    document.getElementById('comp_entry_x').value = offsetX;
    document.getElementById('comp_entry_y').value = offsetY;
    document.querySelectorAll("label").forEach((label) => {
        label.classList.add("active");
    })
}

function initTicketList() {
    window.onload = () => {
        let enterButton = document.getElementById("enter_button");
        if (enterButton != null) {
            enterButton.addEventListener("click", (e) => {
                // updateEntryInputs(e.offsetX, e.offsetY);
                createAndAddTicket();
            });
        }
    };
}

function createAndAddTicket() {
    let ticketList = document.getElementById("ticket_collection");
    let ticketLi = document.createElement("li");
    ticketLi.classList.add("collection-item", "avatar");
    let ticketIcon = document.createElement("i");
    ticketIcon.classList.add("material-icons", "circle", "indigo");
    ticketIcon.innerHTML = "local_activity";
    let ticketTitle = document.createElement("span");
    ticketTitle.classList.add("title");
    ticketTitle.innerHTML = "Title";
    let ticketContent = document.createElement("p");
    ticketContent.innerHTML = "First Line <br> Second Line";
    let ticketDeleteIcon = document.createElement("a");
    ticketDeleteIcon.classList.add()
    ticketLi.append(ticketIcon, ticketTitle, ticketContent);
    ticketList.append(ticketLi);
}

document.addEventListener('DOMContentLoaded', M.AutoInit());