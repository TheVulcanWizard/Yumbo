
function newModelForm(model) {
    var ready = (callback) => {
        if (document.readyState != 'loading') callback();
        else document.addEventListener('DOMContentLoaded', callback);
    }

    ready(() => {
        document.querySelector(`.add-${model}`).addEventListener('click', (e) => {
            e.preventDefault();
            var count = Array.from(document.getElementById(`${model}s-form-container`).children).length
            var template = document.querySelector(`#new-${model}-form-template`).content.cloneNode(true)
            document.querySelector(`div#${model}s-form-container`).append(template);
            document.getElementById(`new-${model}-form`).setAttribute('id', `${model}-${count}`)
            var toReplace = document.getElementById(`${model}-${count}`).innerHTML;
            toReplace = toReplace.replace(/__prefix__/g, count);
            document.getElementById(`${model}-${count}`).innerHTML = toReplace;
            document.getElementById(`delete-${model}-button-${count}`).addEventListener('click', deleteModelForm(model, count))
            var n = 1
            for (var i = 0; i < count+1; i++) {
                if (document.getElementById(`id_${model}_set-${i}-DELETE`).checked == false) {
                    document.getElementById(`id_${model}_set-${i}-position`).value = n
                    n += 1
                }
            }
            document.querySelector(`#id_${model}_set-TOTAL_FORMS`).setAttribute('value', count+1);
        })
    })
}

function deleteModelForm(model, number) {
    var ready = (callback) => {
        if (document.readyState != 'loading') callback();
        else document.addEventListener('DOMContentLoaded', callback);
    }

    ready(() => {
        console.log("Ready!")
        document.querySelector(`#delete-${model}-button-${number}`).addEventListener('click', (e) => {
            e.preventDefault();
            //form will be marked for deletion and hidden from user, but isn't deleted until form is submitted
            document.getElementById(`id_${model}_set-${number}-DELETE`).checked = true;
            document.querySelector(`#${model}-${number}`).style.display = "none";

            //Update "position" value for remaining forms
            var count = Array.from(document.getElementById(`${model}s-form-container`).children).length
            var n = 1
            for (var i = 0; i < count; i++) {
                if (document.getElementById(`id_${model}_set-${i}-DELETE`).checked == false) {
                    document.getElementById(`id_${model}_set-${i}-position`).value = n
                    n += 1
                }
            }
        })
    })
}

// const carousel = document.querySelector("[data-target='carousel'")
// const card = document.querySelector("[data-target='card'")
// const leftButton = document.querySelector("[data-action='slideLeft']")
// const rightButton = document.querySelector("[data-action='slideRight']")

// const carouselWidth = carousel.offsetWidth

// let offset = 0
// const maxOffset = carouselWidth * 8

// leftButton.addEventListener("click", () => {
//     console.log("click left")
//     if (offset !== 0) {
//         offset += carouselWidth
//         carousel.style.transform = `translateX(${offset}px)`
//     }
// })

// rightButton.addEventListener("click", () => {
//     console.log("click right")
//     if (offset !== maxOffset) {
//         offset -= carouselWidth
//         carousel.style.transform = `translateX(${offset}px)`
//     }
// })