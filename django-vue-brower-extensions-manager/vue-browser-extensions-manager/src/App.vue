<script setup>
	import { ref, onMounted } from 'vue';

	const count = ref(0);
	function increment(){
		count++;
	};
	onMounted(() => {
		console.log(`Initiial count:${count}`)
	});
</script>

<template>
	<button @click="count++">Count is: {{ count }}</button>
</template>

<style scoped></style>
