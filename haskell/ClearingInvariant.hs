module ClearingInvariant where

data ClearingLane = ClearingLane
  { laneId :: String
  , debitsEqualCredits :: Bool
  , liquidityHoldReleased :: Bool
  , manualOverrideApproved :: Bool
  , settlementWindowClosed :: Bool
  } deriving (Eq, Show)

invariantPasses :: ClearingLane -> Bool
invariantPasses lane =
  debitsEqualCredits lane
    && liquidityHoldReleased lane
    && manualOverrideApproved lane
    && settlementWindowClosed lane

explainInvariant :: ClearingLane -> String
explainInvariant lane
  | invariantPasses lane = laneId lane ++ ": clearing proof accepted"
  | not (debitsEqualCredits lane) = laneId lane ++ ": debit-credit parity failed"
  | not (liquidityHoldReleased lane) = laneId lane ++ ": liquidity hold remains open"
  | not (manualOverrideApproved lane) = laneId lane ++ ": manual override lacks approval"
  | otherwise = laneId lane ++ ": settlement window remains open"

