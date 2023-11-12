function newtask() {
    var form = document.getElementById("newtask");
    form.style.display = "block";
}

let warningdate = datetime.date.today-timedelta(days=3);

let cautiondate = datetime.date.today-timedelta(days=7);