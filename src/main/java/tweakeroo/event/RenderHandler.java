package tweakeroo.event;

import java.util.function.Supplier;

import net.minecraft.entity.Entity;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.item.ItemMap;
import net.minecraft.item.ItemStack;
import net.minecraft.util.EnumHand;

import malilib.config.value.ActiveMode;
import malilib.event.PostGameOverlayRenderer;
import malilib.event.PostItemTooltipRenderer;
import malilib.event.PostWorldRenderer;
import malilib.gui.BaseScreen;
import malilib.render.BlockTargetingRenderUtils;
import malilib.render.RenderContext;
import malilib.render.inventory.InventoryRenderUtils;
import malilib.util.data.Color4f;
import malilib.util.game.wrap.GameWrap;
import malilib.util.game.wrap.ItemWrap;
import malilib.util.game.wrap.RenderWrap;
import malilib.util.position.HitResult;
import tweakeroo.config.Configs;
import tweakeroo.config.FeatureToggle;
import tweakeroo.config.Hotkeys;
import tweakeroo.renderer.RenderUtils;

public class RenderHandler implements PostGameOverlayRenderer, PostItemTooltipRenderer, PostWorldRenderer
{
    private final Supplier<String> profilerSectionSupplier = () -> "Tweakeroo_RenderHandler";

    @Override
    public Supplier<String> getProfilerSectionSupplier()
    {
        return this.profilerSectionSupplier;
    }

    @Override
    public void onPostGameOverlayRender(RenderContext ctx)
    {
        if (FeatureToggle.TWEAK_HOTBAR_SWAP.getBooleanValue() &&
            Hotkeys.HOTBAR_SWAP_BASE.getKeyBind().isKeyBindHeld())
        {
            RenderUtils.renderHotbarSwapOverlay(ctx);
        }
        else if (FeatureToggle.TWEAK_HOTBAR_SCROLL.getBooleanValue() &&
                 Hotkeys.HOTBAR_SCROLL.getKeyBind().isKeyBindHeld())
        {
            RenderUtils.renderHotbarScrollOverlay(ctx);
        }

        if (FeatureToggle.TWEAK_INVENTORY_PREVIEW.getBooleanValue() &&
            Hotkeys.INVENTORY_PREVIEW.getKeyBind().isKeyBindHeld())
        {
            RenderUtils.renderPointedInventoryOverlay();
        }

        if (FeatureToggle.TWEAK_PLAYER_INVENTORY_PEEK.getBooleanValue() &&
            Hotkeys.PLAYER_INVENTORY_PEEK.getKeyBind().isKeyBindHeld())
        {
            RenderUtils.renderPlayerInventoryPeekOverlay();
        }

        if (FeatureToggle.TWEAK_SNAP_AIM.getBooleanValue() &&
            Configs.Generic.SNAP_AIM_INDICATOR.getBooleanValue())
        {
            RenderUtils.renderSnapAimAngleIndicator(ctx);
        }

        if (FeatureToggle.TWEAK_ELYTRA_CAMERA.getBooleanValue())
        {
            ActiveMode mode = Configs.Generic.ELYTRA_CAMERA_INDICATOR.getValue();

            if (mode == ActiveMode.ALWAYS || (mode == ActiveMode.WITH_KEY && Hotkeys.ELYTRA_CAMERA.getKeyBind().isKeyBindHeld()))
            {
                RenderUtils.renderPitchLockIndicator(ctx);
            }
        }
    }

    @Override
    public void onPostRenderItemTooltip(ItemStack stack, int x, int y, RenderContext ctx)
    {
        float z = Configs.Generic.ITEM_PREVIEW_Z.getIntegerValue();

        if (stack.getItem() instanceof ItemMap)
        {
            if (FeatureToggle.TWEAK_MAP_PREVIEW.getBooleanValue())
            {
                boolean render = Configs.Generic.MAP_PREVIEW_REQUIRE_SHIFT.getBooleanValue() == false || BaseScreen.isShiftDown();

                if (render)
                {
                    int dimensions = Configs.Generic.MAP_PREVIEW_SIZE.getIntegerValue();
                    malilib.render.RenderUtils.renderMapPreview(stack, x, y, z, dimensions, ctx);
                }
            }
        }
        else if (FeatureToggle.TWEAK_SHULKERBOX_DISPLAY.getBooleanValue())
        {
            boolean render = Configs.Generic.SHULKER_DISPLAY_REQUIRE_SHIFT.getBooleanValue() == false || BaseScreen.isShiftDown();

            if (render)
            {
                boolean background = Configs.Generic.SHULKER_DISPLAY_BACKGROUND_COLOR.getBooleanValue();
                x += 8;
                y -= 10;
                InventoryRenderUtils.renderItemInventoryPreview(stack, x, y, z, background, ctx);
            }
        }
    }

    @Override
    public void onPostWorldRender(RenderContext ctx, float tickDelta)
    {
        this.renderOverlays(ctx, tickDelta);
    }

    private void renderOverlays(RenderContext ctx, float tickDelta)
    {
        EntityPlayer player = GameWrap.getClientPlayer();
        HitResult hit = GameWrap.getHitResult();

        if (FeatureToggle.TWEAK_FLEXIBLE_BLOCK_PLACEMENT.getBooleanValue() &&
            hit.type == HitResult.Type.BLOCK &&
            player.isSpectator() == false &&
            (Hotkeys.FLEXIBLE_BLOCK_PLACEMENT_ROTATION.getKeyBind().isKeyBindHeld() ||
             Hotkeys.FLEXIBLE_BLOCK_PLACEMENT_OFFSET.getKeyBind().isKeyBindHeld() ||
             Hotkeys.FLEXIBLE_BLOCK_PLACEMENT_ADJACENT.getKeyBind().isKeyBindHeld()) &&
            (ItemWrap.notEmpty(player.getHeldItem(EnumHand.MAIN_HAND)) ||
             ItemWrap.notEmpty(player.getHeldItem(EnumHand.OFF_HAND))))
        {
            Entity entity = GameWrap.getCameraEntity();
            RenderWrap.depthMask(false);
            RenderWrap.disableLighting();
            RenderWrap.disableCull();
            RenderWrap.disableDepthTest();
            RenderWrap.disableTexture2D();

            RenderWrap.setupBlendSeparate();

            Color4f color = Configs.Generic.FLEXIBLE_PLACEMENT_OVERLAY_COLOR.getColor();

            BlockTargetingRenderUtils.render5WayBlockTargetingOverlay(entity, hit.blockPos, hit.side,
                                                                      hit.pos, color, tickDelta, ctx);

            RenderWrap.enableTexture2D();
            RenderWrap.enableDepthTest();
            RenderWrap.disableBlend();
            RenderWrap.enableCull();
            RenderWrap.depthMask(true);
        }
    }
}
