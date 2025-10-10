<script setup>
	import { ref, onMounted } from 'vue';
	import axios from 'axios';
	import Card from './Card.vue';
	import Page from './Page.vue';

	function convertJSONToCards(cardSort,json){
		json.forEach((card,index) => {
			switch(cardSort){
				case 'all':
					return `<Card card=${card} index=${index}/>`;
				break;
				case 'active':
					if(card.isActive){
						return `<Card card=${card} index=${index}/>`;
					}
				break;
				case 'inactive':
					if(!card.isActive){
						return `<Card card=${card} index=${index}/>`;
					}
				break;
			}
		})
	};

	onMounted(() => {
		axios
			.get("http://127.0.0.1:8000/api/items")
			.then(response => {
					extensionInfo = response.data;
					console.log(response.data)
				}
			 )
			 // convertJSONToCards('all',json)
			 // radioArticle.addEventListener(
			 // 	"change",
			 // 	event => convertJSONToCards(event.target.id,json)
			 // );
		document.querySelector("body")
		.setAttribute("class","darkmode");
	});
</script>

<template>
	<Page />
	<!--
	<main class="side-margin" v-for="(card,index) in cardList">
		<Card/>
	</main>
	-->
</template>

<style src='./style.css'></style>
