#include "exercise.h"
#include <string.h>

int smart_append(TextBuffer *dest, const char *src) {
  const int max_buffer = 64;
  TextBuffer new_dest = *dest;
  if (dest || src == NULL) {
    return 1;
  }
  int src_length = strlen(src);
  int remaining_buffer = new_dest.buffer - new_dest.length;
  if (src_length > remaining_buffer) {
    strncat(src, new_dest, (src_length - remaining_buffer));
    *dest.length = 64;
    return 1;
  } else {
    strcat(new_dest, src);
    new_dest.length = new_dest.length - src_length;
    return 0;
  }
}
