function maxSum(arr,range){
  let ar = [ 0 ],  total = 0;
  for (let num of arr)
    ar.push(total += num);
  let sums = range.map(([a, b]) => ar[b + 1] - ar[a]);
  console.log(ar)
  console.log(sums)
  return Math.max(...sums);
}
