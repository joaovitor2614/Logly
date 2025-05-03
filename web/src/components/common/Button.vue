<script setup lang="ts">
interface Props {
    isDisabled?: boolean,
    isButtonLoading?: boolean,
    id?: string
    buttonAction: () => void
}

const props = withDefaults(defineProps<Props>(), {
    isDisabled: false,
    isButtonLoading: false,
    id: ''
    
})

console.log('isDisabled', props.isDisabled)
</script>


<template>
  <v-btn
    :disabled="props.isDisabled"
    :loading="props.isButtonLoading"
    color="black"
    dark
    :id="props.id"
    @click="props.buttonAction"
  >
    <slot />
  </v-btn>
</template>

<style scoped>

</style>