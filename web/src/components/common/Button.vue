<script setup lang="ts">
interface Props {
    isDisabled?: boolean,
    isButtonLoading?: boolean,
    class?: string,
    id?: string
    buttonAction: () => void
}

const props = withDefaults(defineProps<Props>(), {
    isDisabled: false,
    isButtonLoading: false,
    class: '',
    id: ''
    
})

console.log('isDisabled', props.isDisabled)
</script>


<template>
  <v-btn
    :disabled="props.isDisabled"
    :loading="props.isButtonLoading"
    color="black"
    :class="class"
    dark
    :id="props.id"
    @click="props.buttonAction"
  >
    <slot />
  </v-btn>
</template>

<style scoped>

</style>