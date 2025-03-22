<script setup lang="ts">
interface Props {
  //axis: Plot.Axis;
  comment: App.Comment
}

defineProps<Props>();

const getInitials = (name: string) => {
  return name
    .split(' ')
    .map(word => word.charAt(0).toUpperCase())
    .join('');
};
</script>

<template>
  <v-list-item class="comment">
    <v-avatar color="primary" class="avatar">
      {{ getInitials(comment.author) }}
    </v-avatar>

    <v-list-item-content>
      <v-list-item-title class="author">
        {{ comment.author }}
      </v-list-item-title>
      <v-list-item-subtitle class="timestamp">
        {{ comment.create_time }}
      </v-list-item-subtitle>
      <v-list-item-text class="content">{{ comment.text }}</v-list-item-text>
    </v-list-item-content>
  </v-list-item>

  <v-divider></v-divider>
</template>

<style scoped>
.comment {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 8px;
  border-radius: 8px;
  transition: background 0.2s ease-in-out;
}

.comment:hover {
  background: rgba(0, 0, 0, 0.05);
}

.avatar {
  font-size: 14px;
  font-weight: bold;
  color: white;
}

.author {
  font-weight: bold;
  font-size: 14px;
  color: #333;
}

.timestamp {
  font-size: 12px;
  color: gray;
}

.content {
  font-size: 14px;
  color: #444;
}
</style>