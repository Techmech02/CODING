import React, { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import Image from "next/image";

const hitEffects = {
  head: "🤕 Ouch! My head!",
  body: "😣 That hurt!",
  left: "😵 You hit my left side!",
  right: "😖 My right side is in pain!",
};

export default function AIInteractionGame() {
  const [aiHealth, setAiHealth] = useState(100);
  const [hitEffect, setHitEffect] = useState(null);
  const [aiReaction, setAiReaction] = useState("neutral");

  const handleHit = (event) => {
    const newHealth = Math.max(aiHealth - 10, 0);
    setAiHealth(newHealth);
    
    const x = event.clientX / window.innerWidth;
    const y = event.clientY / window.innerHeight;
    let effect = "😵 That hurt!";
    let reaction = "hurt";

    if (y < 0.3) { effect = hitEffects.head; reaction = "head-hit"; }
    else if (x < 0.4) { effect = hitEffects.left; reaction = "left-hit"; }
    else if (x > 0.6) { effect = hitEffects.right; reaction = "right-hit"; }
    else { effect = hitEffects.body; reaction = "body-hit"; }

    setHitEffect({ text: effect, x: event.clientX, y: event.clientY });
    setAiReaction(reaction);
    
    setTimeout(() => {
      setHitEffect(null);
      setAiReaction("neutral");
    }, 600);
  };

  return (
    <div className="relative w-screen h-screen bg-gray-900 flex items-center justify-center overflow-hidden" onClick={handleHit}>
      <motion.div
        animate={{ opacity: aiHealth > 0 ? 1 : 0, scale: aiReaction === "hurt" ? 1.1 : 1 }}
        transition={{ duration: 0.3 }}
        className="absolute"
      >
        <Image
          src={
            aiReaction === "head-hit" ? "/ai-avatar-head-hit.png" :
            aiReaction === "left-hit" ? "/ai-avatar-left-hit.png" :
            aiReaction === "right-hit" ? "/ai-avatar-right-hit.png" :
            aiReaction === "body-hit" ? "/ai-avatar-body-hit.png" : "/ai-avatar.png"
          }
          alt="AI Avatar"
          width={500}
          height={700}
          className="object-contain"
        />
      </motion.div>

      {hitEffect && (
        <motion.div
          className="absolute text-red-500 text-3xl font-bold"
          style={{ left: hitEffect.x, top: hitEffect.y }}
          initial={{ opacity: 1, scale: 1 }}
          animate={{ opacity: 0, scale: 2 }}
          transition={{ duration: 0.5 }}
        >
          {hitEffect.text}
        </motion.div>
      )}

      <div className="absolute bottom-10 text-white text-xl">
        AI Health: {aiHealth}
      </div>
      <Button className="absolute bottom-5 right-5 bg-red-600 hover:bg-red-700" onClick={() => setAiHealth(100)}>
        Reset AI
      </Button>
    </div>
  );
}

