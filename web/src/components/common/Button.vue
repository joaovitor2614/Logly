<script setup lang="ts">
interface Props {
    isDisabled?: boolean,
    isButtonLoading?: boolean,
    buttonAction: () => void
}

const props = withDefaults(defineProps<Props>(), {
    isDisabled: false,
    isButtonLoading: false,
    
})
</script>


<template>
  <v-btn
    :disabled="props.isDisabled"
    :loading="props.isButtonLoading"
    color="black"
    dark
    @click="props.buttonAction"
  >
    <slot />
  </v-btn>
</template>

<style scoped>

</style>