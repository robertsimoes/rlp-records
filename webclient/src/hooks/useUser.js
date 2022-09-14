import React, { useState, useEffect } from "react";
import { useMemberRepository } from "../hooks/useRepository";

// Squad is a record label records
export const useUserFromWallet = ({walletAddress}) => {
  const [u, setUser] = useState(null);

  const repo = useMemberRepository();

  useEffect(() => {
    repo
      ?.getFromWallet({ walletAddress })
      .then((m) => {

        if (m) {
          console.log("Fetched user from wallet", m.name);
          setUser(m);
        }
      })
      .catch((err) => {
        console.error("Failed to fetch member", err);
        debugger;
      });
  }, [walletAddress, repo]);

  return u;
};
