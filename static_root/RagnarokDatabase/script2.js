const mvps2 =  ['Amon Ra', 'Ancient Anomaly', 'Ancient Tao Gunka', 'Ancient Wootan', 'Angry Dracula', 'Angry Ktullanux',
'Angry Moonlight Flower', 'Arc Bishop Margaretha', 'Assassin Cross Eremes', 'Atroce', 'Awakened Ferre', 'Azure Princess', 'Bacsojin',
'Bakonawa', 'Bangungot', 'Baphomet', 'Beelzebub', 'Bijou', 'Boitata', 'Bone Detardeurus', 'Boss Egnigem', 'Boss Meow', 'Broken Memory of Thanatos',
'Buwaya', 'Captain Ferlock', 'Celine Kimi', 'Champion Chen', 'Chaotic Baphomet', 'Charleston 3', 'Clown Alphoccio', 'Corrupted Dark Lord', 'Corrupted Spider Queen',
 'Corruption Root', 'Creator Flamel', 'Cursed King Schmidt', 'Cutie', 'Daehyon', 'Dark Coelacanth', 'Dark Guardian Kades', 'Dark Lord', 'Deep Sea Kraken',
  'Deep Sea Witch', 'Despair God Morocc', 'Detardeurus', 'Doppelganger']
;


const ulEl2 = document.querySelector("#mvp_list2")
const d = new Date();
let daynumber = d.getMonth() == 1 ? d.getDate() - 1 : 0;
let activeIndex = daynumber;
const rotate = -360 / mvps2.length;
init();

function init() {
	mvps2.forEach((holiday, idx) => {
		const liEl2 = document.createElement(".mvp_list2 li");
		liEl2.style.setProperty("--day_idx", idx);
		liEl2.innerHTML = `<time datetime="2022-02-${idx + 1}">${
			idx + 1
		}</time><span>${holiday}</span>`;
		ulEl2.append(liEl);
	});
	ulEl2.style.setProperty("--rotateDegrees", rotate);
	adjustDay(0);
}

function adjustDay2(nr) {
	daynumber += nr;
	ulEl2.style.setProperty("--currentDay", daynumber);

	const activeEl2 = document.querySelector("li.active");
	if (activeEl2) activeEl.classList.remove("active");

	activeIndex2 = (activeIndex2 + nr + mvps2.length) % mvps2.length;
	const newActiveEl2 = document.querySelector(`li:nth-child(${activeIndex2 + 1})`);
	document.body.style.backgroundColor = window.getComputedStyle(
		newActiveEl2
	).backgroundColor;

	newActiveEl2.classList.add("active");
}

window.addEventListener("keydown", (e) => {
	switch (e.key) {
		case "ArrowUp":
			adjustDay(-1);
			break;
		case "ArrowDown":
			adjustDay(1);
			break;
		default:
			return;
	}
});
