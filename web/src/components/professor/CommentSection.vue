<script setup lang="ts">
import { ref } from 'vue';
import Comment from './Comment.vue';


interface Comment {
  id: number;
  author: string;
  content: string;
  timestamp: string;
}

const comments = ref<Comment[]>([
  { id: 1, author: 'John Doe', content: 'Great professor!', timestamp: '2 hours ago' },
  { id: 2, author: 'Jane Smith', content: 'Very knowledgeable.', timestamp: '1 hour ago' },
]);

const newComment = ref('');

const addComment = () => {
  if (!newComment.value.trim()) return;

  comments.value.unshift({
    id: comments.value.length + 1,
    author: 'You',
    content: newComment.value,
    timestamp: 'Just now',
  });

  newComment.value = '';
};
</script>

<template>
  <v-card class="pa-4 comment-section">
    <v-card-title class="title">Comments</v-card-title>
    <v-divider></v-divider>

    <v-list class="comments-list">
      <transition-group name="fade">
        <Comment v-for="comment in comments" :key="comment.id" :comment="comment" />
      </transition-group>
    </v-list>

    <v-divider class="my-3"></v-divider>

    <v-textarea
      v-model="newComment"
      label="Write a comment..."
      auto-grow
      rows="2"
      variant="outlined"
      class="custom-textarea"
    ></v-textarea>

    <v-btn color="primary" block class="post-btn" @click="addComment">Post Comment</v-btn>
  </v-card>
</template>

<style scoped>
.comment-section {
  border-radius: 12px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  background: #fff;
  max-width: 600px;
  margin: auto;
}

.title {
  font-size: 20px;
  font-weight: bold;
  color: #333;
}

.comments-list {
  max-height: 300px;
  overflow-y: auto;
  padding: 8px 0;
}

.custom-textarea {
  background: #f8f9fa;
  border-radius: 8px;
}

.post-btn {
  font-weight: 600;
  border-radius: 8px;
  margin-top: 10px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>