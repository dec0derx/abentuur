function uploadFiles() {
    const filesInput = document.getElementById("files");
    const files = filesInput.files;

    if (!files.length) {
        alert("Please select files");
        return;
    }

    const formData = new FormData();

    for (let file of files) {
        formData.append("files", file);
    }

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);

    xhr.upload.onprogress = function(event) {
        if (event.lengthComputable) {
            const percent = Math.round(
                (event.loaded / event.total) * 100
            );

            document.getElementById("progressBar").value = percent;
            document.getElementById("progressText").innerText =
                percent + "%";
        }
    };

    xhr.onload = function() {
        document.getElementById("status").innerHTML =
            xhr.responseText;
    };

    xhr.send(formData);
}