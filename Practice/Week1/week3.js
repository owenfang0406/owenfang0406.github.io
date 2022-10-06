let storedObjects = []

function hide() {
    var checkbox = document.getElementById('checkbox');
    if (checkbox.checked) {
        checkbox.checked = false;
    }
}

function splitFile(file) {
    const splitFile = file.split("https://")
    return splitFile
}

function handleData(json) {
    objects = [];
    for (let i = 0; i < json.length; i++) {
        const title = json[i]["stitle"];
        const file = splitFile(json[i]["file"]);
        objects.push({
            title: title,
            file: file
        })
    }
    return objects
}

fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
    .then((response) => {
        return response.json();
    })
    .then((json) => {
        objects = handleData(json["result"]["results"]);
        storedObjects = objects
        let n = 0;
        const box = document.querySelectorAll("#boxContainer");
        const longBox = document.querySelectorAll("#longBox")

        for (i = 0; i < 2; i++) {
            const filePic = "https://" + objects[i + 1]["file"][1];
            const image = document.createElement("img");
            const titles = objects[i]["title"]
            const title = document.createElement("div")
            image.src = filePic;
            image.classList.add("longBoxImg");
            longBox[i].appendChild(image);
            title.classList.add("innerLongBox");
            title.innerText = titles;
            longBox[i].appendChild(title);

        }
        for (i = 0; i < (box.length + 2); i++) {
            const filePic = "https://" + objects[i + 2]["file"][1]
            const image = document.createElement("img");
            const titles = objects[i + 2]["title"]
            const title = document.createElement("div")
            image.src = filePic;
            image.classList.add("boxImg");
            box[i].appendChild(image);
            title.classList.add("title");
            title.innerText = titles;
            box[i].appendChild(title);



        }

    })

let pageIndex = 0;

const box = document.querySelectorAll("#boxContainer")
const boxContainer = document.getElementById("container2")
function clickLoadMore() {
    for (let i = (8 * pageIndex); i < 8 * (pageIndex + 1); i++) {
        const filePic = "https://" + storedObjects[i + 10]["file"][1]
        const newBox = document.createElement("div");
        const newImg = document.createElement("img");
        const titles = storedObjects[i + 10]["title"];
        const title = document.createElement("div");
        newBox.classList.add("boxContainer");
        newBox.setAttribute("id", "boxContainer");
        boxContainer.appendChild(newBox);
        newImg.classList.add("boxImg");
        newImg.src = filePic;
        newBox.appendChild(newImg);
        title.classList.add("title");
        title.innerText = titles;
        newBox.append(title);
        console.log(i);

        if (i == (storedObjects.length - 11)) {
            const btn = document.getElementById("btn");
            btn.style.display = "none";
        }

    }
    pageIndex += 1;

}