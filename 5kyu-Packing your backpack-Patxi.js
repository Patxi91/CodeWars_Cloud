function packBagpack(scores, weights, capacity) {
  let arr = Array.from({ length: capacity + 1 }, () => 0);
  for (let i = 0; i < weights.length; i++)
    arr = arr.map((l, w) => Math.max(l, weights[i] <= w && arr[w - weights[i]] + scores[i]));
  return arr.pop();
}