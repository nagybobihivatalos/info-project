let currentImageIndex = 0;
const images = [
    "teljesgep.jpg",
    "part1.jpg", "part2.jpg", "part3.jpg", "part4.jpg", "part5.jpg",
    "part6.jpg", "part7.jpg", "part8.jpg", "part9.jpg", "part10.jpg"
];

function openModal(index) {
    currentImageIndex = index;
    const modal = document.getElementById('imageModal');
    const modalImage = document.getElementById('modalImage');
    const caption = document.getElementById('caption');
    
    modal.style.display = "block";
    modalImage.src = images[index];
   
}

function closeModal() {
    document.getElementById('imageModal').style.display = "none";
}

function changeImage(direction) {
    currentImageIndex += direction;
    if (currentImageIndex < 0) currentImageIndex = images.length - 1;
    if (currentImageIndex >= images.length) currentImageIndex = 0;

    const modalImage = document.getElementById('modalImage');
    const caption = document.getElementById('caption');
    
    modalImage.src = images[currentImageIndex];
    caption.textContent = `Kép ${currentImageIndex + 1}`;
}
