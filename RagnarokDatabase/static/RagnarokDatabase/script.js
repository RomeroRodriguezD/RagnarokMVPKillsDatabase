const febHolidays =  ['Amon Ra', 'Ancient Anomaly', 'Ancient Tao Gunka', 'Ancient Wootan', 'Angry Dracula', 'Angry Ktullanux', 'Angry Moonlight Flower', 'Arc Bishop Margaretha', 'Assassin Cross Eremes', 'Atroce', 'Awakened Ferre', 'Azure Princess', 'Bacsojin', 'Bakonawa', 'Bangungot', 'Baphomet', 'Beelzebub', 'Bijou', 'Boitata', 'Bone Detardeurus', 'Boss Egnigem', 'Boss Meow', 'Broken Memory of Thanatos', 'Buwaya', 'Captain Ferlock', 'Celine Kimi', 'Champion Chen', 'Chaotic Baphomet', 'Charleston 3', 'Clown Alphoccio', 'Corrupted Dark Lord', 'Corrupted Spider Queen', 'Corruption Root', 'Creator Flamel', 'Cursed King Schmidt', 'Cutie', 'Daehyon', 'Dark Coelacanth', 'Dark Guardian Kades', 'Dark Lord', 'Deep Sea Kraken', 'Deep Sea Witch', 'Despair God Morocc', 'Detardeurus', 'Doppelganger', 'Dracula', 'Drake', 'Eddga', 'EL1-A17T', 'Entweihen Crothen', 'Evil Believer', 'Evil Snake Lord', 'Faceworm Queen', 'Fallen Bishop Hibram', 'Fenrir', 'Geneticist Flamel', 'Giant Eggring', 'Giant Octopus', 'Gipsy Trentini', 'Gloom Under Night', 'Gold Queen Scaraba', 'Golden Thief Bug', 'Gopinich', 'Grand Papilia', 'Great Demon Baphomet', 'Greater Red Pepper', 'Grim Reaper Ankou', 'Guillotine Cross Eremes', 'Hatii', 'Heart Hunter Evil', 'High Priest Magaleta', 'High Wizard Katrinn', 'Ifrit', 'Incantation Samurai', 'Infinite Eddga', 'Infinite Orc Hero', 'Infinite Osiris', 'Infinite Phreeoni', 'Infinite Tao Gunka', 'Ingrid', 'Jungoliant', 'Kiel D-01', 'Kraken', 'Ktullanux', 'Lady Tanee', 'Leak', 'Lich Lord', 'Lord Knight Seyren', 'Lord of Death', 'Lost Dragon', 'Maya', 'Mechanic Howard', 'Memory of Thanatos', 'Miguel', 'Minstrel Alphoccio', 'Mistress', 'Moonlight Flower', 'Morroc Necromancer', 'Mutant Coelacanth', 'Naght Sieger', 'Nameless Swordman', 'Nidhogg Shadow', 'Nightmare Amon Ra', 'Nightmare Baphomet', 'Ominous Turtle General', 'Orc Hero', 'Orc Lord', 'Osiris', 'Paladin Randel', 'Phantom Amdarais', 'Phantom Himmelmez', 'Pharaoh', 'Phreeoni', 'Professor Celia', 'Pyuriel', 'Queen Scaraba', 'R-48-85-BESTIA', 'Randgris', 'Rangel Cecil', 'Realized Amdarais', 'Realized Corruption Root', 'Red Pepper', 'Reginleif', 'Rigid Muspellskoll', 'Royal Guard Randel', 'RSX 0806', 'Rune Knight Seyren', 'Sarah', 'Shadow Chaser Gertie', 'Shiny Teddy Bear', 'Silent Maya', 'Silva Papilia', 'Sniper Cecil', 'Sorcerer Celia', 'Spider Chariot', 'Stalker Gertie', 'Staphen Jack Ernest Wolf', 'Stormy Knight', 'Sura Chen', 'Sweetie', 'T_W_O', 'Tao Gunka', 'Time Holder', 'Toxic Chimera', 'Turtle General', 'Vesper', 'Violent Coelacanth', 'Weird Coelacanth', 'Whitesmith Howard', 'YSF01 Seyren']

;


const ulEl = document.querySelector("ul");
const d = new Date();
let daynumber = d.getMonth() == 1 ? d.getDate() - 1 : 0;
let activeIndex = daynumber;
const rotate = -360 / febHolidays.length;
init();

function init() {
	febHolidays.forEach((holiday, idx) => {
		const liEl = document.createElement("li");
		liEl.style.setProperty("--day_idx", idx);
		liEl.innerHTML = `<time datetime="2022-02-${idx + 1}"></time><span>${holiday}</span>`;
		ulEl.append(liEl);
	});
	ulEl.style.setProperty("--rotateDegrees", rotate);
	adjustDay(0);
}

function adjustDay(nr) {
	daynumber += nr;
	ulEl.style.setProperty("--currentDay", daynumber);

	const activeEl = document.querySelector("li.active");
	if (activeEl) activeEl.classList.remove("active");

	activeIndex = (activeIndex + nr + febHolidays.length) % febHolidays.length;
	const newActiveEl = document.querySelector(`li:nth-child(${activeIndex + 1})`);



	newActiveEl.classList.add("active");
}

window.addEventListener("keydown", (e) => {
	switch (e.key) {
		case "ArrowUp":
			adjustDay(-1);
			break;
		case "ArrowDown":
			adjustDay(1);
			break;
		case "a":
		    adjustDay(50)
		    break
		default:
			return;
	}
});

