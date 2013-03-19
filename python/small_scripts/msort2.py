#!/usr/bin/python

import sys

def mergesort(l):
  size = len(l)
  if size < 2:
    return l

  mid = size / 2
  left = mergesort(l[0:mid])
  right = mergesort(l[mid:])
  return merge(left, right)

def merge(left, right):
  left_len = len(left)
  right_len = len(right)
  i = 0
  j = 0
  res = []

  while i < left_len or j < right_len:
    if i == left_len:
      res.append(right[j])
      j += 1
      continue

    if j == right_len:
      res.append(left[i])
      i += 1
      continue

    if left[i] < right[j]:
      res.append(left[i])
      i += 1
    else:
      res.append(right[j])
      j += 1

  return res
   

