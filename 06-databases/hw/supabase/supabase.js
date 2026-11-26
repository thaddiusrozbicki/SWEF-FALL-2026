import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.50.0/+esm";

const SUPABASE_URL = "https://xrlpybmftplxtdtmsnjf.supabase.co";
const SUPABASE_ANON_KEY = "sb_publishable_b3Ryk-Tx_6T9gHINi9Z45Q_--oIaAAl";

export const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
